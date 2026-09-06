# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 386
- HTTP: 142 alive / 78 gold
- HTTPS: 54 alive / 25 gold
- SOCKS4: 157 alive / 135 gold
- SOCKS5: 177 alive / 148 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48023
- Ever gold: 1511

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
