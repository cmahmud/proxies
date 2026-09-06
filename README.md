# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 384
- HTTP: 142 alive / 78 gold
- HTTPS: 58 alive / 24 gold
- SOCKS4: 160 alive / 132 gold
- SOCKS5: 181 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48015
- Ever gold: 1511

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
