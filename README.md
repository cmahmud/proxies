# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 425
- HTTP: 105 alive / 69 gold
- HTTPS: 35 alive / 19 gold
- SOCKS4: 183 alive / 164 gold
- SOCKS5: 191 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48963
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
