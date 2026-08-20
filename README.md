# SyndProxy private pool

## Current pool

- Alive now: 742
- Gold now: 370
- HTTP: 237 alive / 59 gold
- HTTPS: 102 alive / 18 gold
- SOCKS4: 194 alive / 149 gold
- SOCKS5: 209 alive / 144 gold

## Historical pool

- Discovered: 146664
- Ever alive: 25745
- Ever gold: 1074

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
