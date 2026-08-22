# SyndProxy private pool

## Current pool

- Alive now: 1018
- Gold now: 385
- HTTP: 331 alive / 84 gold
- HTTPS: 238 alive / 26 gold
- SOCKS4: 205 alive / 123 gold
- SOCKS5: 244 alive / 152 gold

## Historical pool

- Discovered: 164976
- Ever alive: 32266
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
