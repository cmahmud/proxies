# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 414
- HTTP: 121 alive / 84 gold
- HTTPS: 65 alive / 26 gold
- SOCKS4: 165 alive / 145 gold
- SOCKS5: 184 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48050
- Ever gold: 1516

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
