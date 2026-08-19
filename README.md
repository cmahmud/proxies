# SyndProxy private pool

## Current pool

- Alive now: 918
- Gold now: 416
- HTTP: 304 alive / 90 gold
- HTTPS: 227 alive / 72 gold
- SOCKS4: 190 alive / 125 gold
- SOCKS5: 197 alive / 129 gold

## Historical pool

- Discovered: 127417
- Ever alive: 19981
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
