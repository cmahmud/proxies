# SyndProxy private pool

## Current pool

- Alive now: 740
- Gold now: 396
- HTTP: 185 alive / 87 gold
- HTTPS: 123 alive / 21 gold
- SOCKS4: 211 alive / 136 gold
- SOCKS5: 221 alive / 152 gold

## Historical pool

- Discovered: 154732
- Ever alive: 29181
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
