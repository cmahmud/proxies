# SyndProxy private pool

## Current pool

- Alive now: 871
- Gold now: 212
- HTTP: 256 alive / 24 gold
- HTTPS: 186 alive / 8 gold
- SOCKS4: 201 alive / 96 gold
- SOCKS5: 228 alive / 84 gold

## Historical pool

- Discovered: 91698
- Ever alive: 8641
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
