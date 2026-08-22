# SyndProxy private pool

## Current pool

- Alive now: 987
- Gold now: 397
- HTTP: 247 alive / 88 gold
- HTTPS: 242 alive / 26 gold
- SOCKS4: 236 alive / 136 gold
- SOCKS5: 262 alive / 147 gold

## Historical pool

- Discovered: 164253
- Ever alive: 32111
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
