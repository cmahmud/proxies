# SyndProxy private pool

## Current pool

- Alive now: 810
- Gold now: 334
- HTTP: 247 alive / 82 gold
- HTTPS: 181 alive / 22 gold
- SOCKS4: 172 alive / 103 gold
- SOCKS5: 210 alive / 127 gold

## Historical pool

- Discovered: 157573
- Ever alive: 29770
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
