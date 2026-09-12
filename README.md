# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 465
- HTTP: 128 alive / 94 gold
- HTTPS: 70 alive / 36 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 197 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49392
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
