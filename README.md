# SyndProxy private pool

## Current pool

- Alive now: 983
- Gold now: 526
- HTTP: 325 alive / 163 gold
- HTTPS: 258 alive / 92 gold
- SOCKS4: 198 alive / 141 gold
- SOCKS5: 202 alive / 130 gold

## Historical pool

- Discovered: 119845
- Ever alive: 18403
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
