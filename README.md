# SyndProxy private pool

## Current pool

- Alive now: 742
- Gold now: 394
- HTTP: 187 alive / 74 gold
- HTTPS: 122 alive / 21 gold
- SOCKS4: 221 alive / 144 gold
- SOCKS5: 212 alive / 155 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25502
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
