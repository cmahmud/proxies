# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 387
- HTTP: 212 alive / 81 gold
- HTTPS: 255 alive / 24 gold
- SOCKS4: 212 alive / 145 gold
- SOCKS5: 203 alive / 137 gold

## Historical pool

- Discovered: 163332
- Ever alive: 31871
- Ever gold: 1168

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
