# SyndProxy validated proxy pool

## Current pool

- Alive now: 386
- Gold now: 298
- HTTP: 101 alive / 77 gold
- HTTPS: 59 alive / 22 gold
- SOCKS4: 73 alive / 67 gold
- SOCKS5: 153 alive / 132 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47915
- Ever gold: 1503

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
