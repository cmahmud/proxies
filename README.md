# SyndProxy private pool

## Current pool

- Alive now: 1737
- Gold now: 628
- HTTP: 646 alive / 213 gold
- HTTPS: 490 alive / 116 gold
- SOCKS4: 226 alive / 136 gold
- SOCKS5: 375 alive / 163 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23926
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
