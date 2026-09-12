# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 435
- HTTP: 110 alive / 86 gold
- HTTPS: 54 alive / 32 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 181 alive / 160 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49436
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
