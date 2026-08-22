# SyndProxy private pool

## Current pool

- Alive now: 807
- Gold now: 405
- HTTP: 222 alive / 94 gold
- HTTPS: 171 alive / 30 gold
- SOCKS4: 173 alive / 123 gold
- SOCKS5: 241 alive / 158 gold

## Historical pool

- Discovered: 167131
- Ever alive: 32550
- Ever gold: 1188

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
