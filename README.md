# SyndProxy private pool

## Current pool

- Alive now: 1019
- Gold now: 256
- HTTP: 392 alive / 32 gold
- HTTPS: 171 alive / 5 gold
- SOCKS4: 226 alive / 116 gold
- SOCKS5: 230 alive / 103 gold

## Historical pool

- Discovered: 95404
- Ever alive: 10982
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
