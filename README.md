# SyndProxy private pool

## Current pool

- Alive now: 1958
- Gold now: 698
- HTTP: 779 alive / 236 gold
- HTTPS: 633 alive / 147 gold
- SOCKS4: 224 alive / 148 gold
- SOCKS5: 322 alive / 167 gold

## Historical pool

- Discovered: 142715
- Ever alive: 24466
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
