# SyndProxy validated proxy pool

## Current pool

- Alive now: 437
- Gold now: 356
- HTTP: 71 alive / 42 gold
- HTTPS: 28 alive / 9 gold
- SOCKS4: 164 alive / 153 gold
- SOCKS5: 174 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48300
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
