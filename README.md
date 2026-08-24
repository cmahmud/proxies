# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 386
- HTTP: 128 alive / 65 gold
- HTTPS: 55 alive / 14 gold
- SOCKS4: 171 alive / 155 gold
- SOCKS5: 175 alive / 152 gold

## Historical pool

- Discovered: 176968
- Ever alive: 33254
- Ever gold: 1232

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
