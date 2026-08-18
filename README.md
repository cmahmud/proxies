# SyndProxy private pool

## Current pool

- Alive now: 871
- Gold now: 266
- HTTP: 252 alive / 33 gold
- HTTPS: 197 alive / 5 gold
- SOCKS4: 209 alive / 119 gold
- SOCKS5: 213 alive / 109 gold

## Historical pool

- Discovered: 99124
- Ever alive: 11877
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
