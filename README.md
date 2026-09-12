# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 469
- HTTP: 129 alive / 94 gold
- HTTPS: 52 alive / 35 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 190 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49396
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
