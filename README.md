# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 382
- HTTP: 125 alive / 69 gold
- HTTPS: 98 alive / 13 gold
- SOCKS4: 164 alive / 149 gold
- SOCKS5: 186 alive / 151 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33234
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
