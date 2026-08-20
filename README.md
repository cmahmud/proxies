# SyndProxy private pool

## Current pool

- Alive now: 1521
- Gold now: 636
- HTTP: 579 alive / 235 gold
- HTTPS: 479 alive / 121 gold
- SOCKS4: 205 alive / 136 gold
- SOCKS5: 258 alive / 144 gold

## Historical pool

- Discovered: 142729
- Ever alive: 24573
- Ever gold: 1028

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
