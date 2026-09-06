# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 392
- HTTP: 102 alive / 73 gold
- HTTPS: 47 alive / 12 gold
- SOCKS4: 165 alive / 153 gold
- SOCKS5: 183 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48103
- Ever gold: 1519

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
