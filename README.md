# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 395
- HTTP: 109 alive / 78 gold
- HTTPS: 45 alive / 14 gold
- SOCKS4: 163 alive / 152 gold
- SOCKS5: 177 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48198
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
