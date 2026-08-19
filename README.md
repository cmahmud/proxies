# SyndProxy private pool

## Current pool

- Alive now: 1019
- Gold now: 525
- HTTP: 312 alive / 154 gold
- HTTPS: 281 alive / 104 gold
- SOCKS4: 221 alive / 144 gold
- SOCKS5: 205 alive / 123 gold

## Historical pool

- Discovered: 127380
- Ever alive: 19958
- Ever gold: 806

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
