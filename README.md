# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 413
- HTTP: 321 alive / 88 gold
- HTTPS: 202 alive / 23 gold
- SOCKS4: 212 alive / 155 gold
- SOCKS5: 243 alive / 147 gold

## Historical pool

- Discovered: 158253
- Ever alive: 30072
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
