# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 449
- HTTP: 99 alive / 76 gold
- HTTPS: 109 alive / 29 gold
- SOCKS4: 174 alive / 164 gold
- SOCKS5: 197 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47419
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
