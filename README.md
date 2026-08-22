# SyndProxy private pool

## Current pool

- Alive now: 850
- Gold now: 372
- HTTP: 250 alive / 67 gold
- HTTPS: 175 alive / 23 gold
- SOCKS4: 199 alive / 125 gold
- SOCKS5: 226 alive / 157 gold

## Historical pool

- Discovered: 164971
- Ever alive: 32252
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
