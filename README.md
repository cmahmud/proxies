# SyndProxy private pool

## Current pool

- Alive now: 957
- Gold now: 399
- HTTP: 315 alive / 86 gold
- HTTPS: 225 alive / 27 gold
- SOCKS4: 192 alive / 132 gold
- SOCKS5: 225 alive / 154 gold

## Historical pool

- Discovered: 144731
- Ever alive: 24933
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
