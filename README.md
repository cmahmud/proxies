# SyndProxy private pool

## Current pool

- Alive now: 1678
- Gold now: 617
- HTTP: 622 alive / 213 gold
- HTTPS: 474 alive / 115 gold
- SOCKS4: 220 alive / 136 gold
- SOCKS5: 362 alive / 153 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23925
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
