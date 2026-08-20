# SyndProxy private pool

## Current pool

- Alive now: 1639
- Gold now: 598
- HTTP: 616 alive / 212 gold
- HTTPS: 497 alive / 109 gold
- SOCKS4: 203 alive / 135 gold
- SOCKS5: 323 alive / 142 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23866
- Ever gold: 962

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
