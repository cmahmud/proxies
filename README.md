# SyndProxy private pool

## Current pool

- Alive now: 871
- Gold now: 393
- HTTP: 256 alive / 89 gold
- HTTPS: 179 alive / 25 gold
- SOCKS4: 205 alive / 132 gold
- SOCKS5: 231 alive / 147 gold

## Historical pool

- Discovered: 161996
- Ever alive: 31337
- Ever gold: 1157

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
