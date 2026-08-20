# SyndProxy private pool

## Current pool

- Alive now: 778
- Gold now: 352
- HTTP: 194 alive / 65 gold
- HTTPS: 137 alive / 18 gold
- SOCKS4: 230 alive / 144 gold
- SOCKS5: 217 alive / 125 gold

## Historical pool

- Discovered: 145548
- Ever alive: 25393
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
