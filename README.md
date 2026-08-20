# SyndProxy private pool

## Current pool

- Alive now: 881
- Gold now: 400
- HTTP: 258 alive / 84 gold
- HTTPS: 197 alive / 25 gold
- SOCKS4: 214 alive / 147 gold
- SOCKS5: 212 alive / 144 gold

## Historical pool

- Discovered: 151072
- Ever alive: 27477
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
