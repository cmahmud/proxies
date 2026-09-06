# SyndProxy validated proxy pool

## Current pool

- Alive now: 446
- Gold now: 360
- HTTP: 77 alive / 45 gold
- HTTPS: 30 alive / 11 gold
- SOCKS4: 164 alive / 153 gold
- SOCKS5: 175 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48309
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
