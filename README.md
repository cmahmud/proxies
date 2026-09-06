# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 405
- HTTP: 110 alive / 79 gold
- HTTPS: 60 alive / 21 gold
- SOCKS4: 164 alive / 147 gold
- SOCKS5: 184 alive / 158 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48053
- Ever gold: 1516

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
