# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 462
- HTTP: 141 alive / 93 gold
- HTTPS: 111 alive / 32 gold
- SOCKS4: 187 alive / 162 gold
- SOCKS5: 206 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46305
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
