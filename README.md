# SyndProxy private pool

## Current pool

- Alive now: 1623
- Gold now: 629
- HTTP: 559 alive / 209 gold
- HTTPS: 487 alive / 116 gold
- SOCKS4: 237 alive / 146 gold
- SOCKS5: 340 alive / 158 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24059
- Ever gold: 968

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
