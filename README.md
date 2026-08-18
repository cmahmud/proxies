# SyndProxy private pool

## Current pool

- Alive now: 807
- Gold now: 256
- HTTP: 210 alive / 32 gold
- HTTPS: 125 alive / 8 gold
- SOCKS4: 243 alive / 124 gold
- SOCKS5: 229 alive / 92 gold

## Historical pool

- Discovered: 91720
- Ever alive: 9106
- Ever gold: 362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
