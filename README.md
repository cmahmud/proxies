# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 370
- HTTP: 350 alive / 80 gold
- HTTPS: 238 alive / 24 gold
- SOCKS4: 223 alive / 125 gold
- SOCKS5: 231 alive / 141 gold

## Historical pool

- Discovered: 165816
- Ever alive: 32324
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
