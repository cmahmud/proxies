# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 384
- HTTP: 119 alive / 63 gold
- HTTPS: 51 alive / 15 gold
- SOCKS4: 172 alive / 154 gold
- SOCKS5: 176 alive / 152 gold

## Historical pool

- Discovered: 176968
- Ever alive: 33255
- Ever gold: 1232

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
