# SyndProxy private pool

## Current pool

- Alive now: 853
- Gold now: 283
- HTTP: 254 alive / 25 gold
- HTTPS: 143 alive / 5 gold
- SOCKS4: 240 alive / 144 gold
- SOCKS5: 216 alive / 109 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12364
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
