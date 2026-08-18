# SyndProxy private pool

## Current pool

- Alive now: 724
- Gold now: 247
- HTTP: 189 alive / 28 gold
- HTTPS: 103 alive / 6 gold
- SOCKS4: 222 alive / 121 gold
- SOCKS5: 210 alive / 92 gold

## Historical pool

- Discovered: 91738
- Ever alive: 9107
- Ever gold: 362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
