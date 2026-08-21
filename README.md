# SyndProxy private pool

## Current pool

- Alive now: 833
- Gold now: 361
- HTTP: 240 alive / 82 gold
- HTTPS: 201 alive / 27 gold
- SOCKS4: 181 alive / 120 gold
- SOCKS5: 211 alive / 132 gold

## Historical pool

- Discovered: 157573
- Ever alive: 29776
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
