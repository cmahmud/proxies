# SyndProxy private pool

## Current pool

- Alive now: 1157
- Gold now: 545
- HTTP: 425 alive / 191 gold
- HTTPS: 315 alive / 82 gold
- SOCKS4: 211 alive / 129 gold
- SOCKS5: 206 alive / 143 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19827
- Ever gold: 801

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
