# SyndProxy private pool

## Current pool

- Alive now: 1638
- Gold now: 624
- HTTP: 580 alive / 209 gold
- HTTPS: 453 alive / 117 gold
- SOCKS4: 237 alive / 144 gold
- SOCKS5: 368 alive / 154 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24067
- Ever gold: 968

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
