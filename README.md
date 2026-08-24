# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 384
- HTTP: 113 alive / 64 gold
- HTTPS: 63 alive / 15 gold
- SOCKS4: 169 alive / 153 gold
- SOCKS5: 173 alive / 152 gold

## Historical pool

- Discovered: 176968
- Ever alive: 33254
- Ever gold: 1232

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
