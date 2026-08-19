# SyndProxy private pool

## Current pool

- Alive now: 1186
- Gold now: 556
- HTTP: 433 alive / 188 gold
- HTTPS: 302 alive / 98 gold
- SOCKS4: 215 alive / 123 gold
- SOCKS5: 236 alive / 147 gold

## Historical pool

- Discovered: 124835
- Ever alive: 19253
- Ever gold: 770

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
