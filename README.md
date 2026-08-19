# SyndProxy private pool

## Current pool

- Alive now: 1118
- Gold now: 516
- HTTP: 417 alive / 154 gold
- HTTPS: 293 alive / 86 gold
- SOCKS4: 206 alive / 142 gold
- SOCKS5: 202 alive / 134 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18505
- Ever gold: 719

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
