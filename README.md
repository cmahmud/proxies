# SyndProxy private pool

## Current pool

- Alive now: 1512
- Gold now: 584
- HTTP: 546 alive / 192 gold
- HTTPS: 464 alive / 91 gold
- SOCKS4: 244 alive / 144 gold
- SOCKS5: 258 alive / 157 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24050
- Ever gold: 968

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
